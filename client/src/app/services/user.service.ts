import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { environment } from "src/environments/environment";

import { User } from "../models/User";
import { Observable } from "rxjs";

@Injectable({
  providedIn: "root"
})
export class UserService {
  constructor(private httpClient:HttpClient) {}

  getUsers():Observable<User[]> {
    const url = `${[environment.API_URL]}/api/users`;
    return this.httpClient.get<User[]>(url);
  }
}
