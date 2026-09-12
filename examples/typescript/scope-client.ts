/** Server-only client: supply secrets from environment, never from browser code. */
export class ScopeApiError extends Error {
  constructor(public status: number, public body: unknown) { super(`Scope API returned HTTP ${status}`); }
}
export class ScopeClient {
  constructor(private baseURL: string, private apiKey: string) {}
  async request<T>(method: string, path: string, options: {query?:Record<string,string>;body?:unknown;requestKey?:string;maxCents?:number;etag?:string} = {}) {
    const headers = new Headers({authorization:`Bearer ${this.apiKey}`,accept:"application/json"});
    if(options.requestKey)headers.set("Idempotency-Key",options.requestKey);
    if(options.maxCents!==undefined)headers.set("X-Max-Charge-Cents",String(options.maxCents));
    if(options.etag)headers.set("If-None-Match",options.etag);
    if(options.body!==undefined)headers.set("content-type","application/json");
    const query = options.query?`?${new URLSearchParams(options.query)}`:"";
    const response=await fetch(`${this.baseURL.replace(/\/$/,"")}/api/v1${path}${query}`,{method,headers,
      body:options.body===undefined?undefined:JSON.stringify(options.body),signal:AbortSignal.timeout(30000),redirect:"error"});
    if(response.status===304)return {status:304,etag:response.headers.get("etag"),body:null};
    const body:unknown=await response.json();
    if(!response.ok)throw new ScopeApiError(response.status,body);
    return {status:response.status,etag:response.headers.get("etag"),body:body as T};
  }
  accept(requestKey:string,quoteId:string,maxCents:number){return this.request("POST","/geo/checks",{requestKey,body:{quote_id:quoteId,max_charge_cents:maxCents}});}
}
