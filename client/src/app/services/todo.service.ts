import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { environment } from "src/environments/environment";

import { Todo } from "../models/Todo";
import { Observable } from "rxjs";

@Injectable({
  providedIn: "root"
})
export class TodoService {
  constructor(private httpClient:HttpClient) {}

  getTodos():Observable<Todo[]> {
    const url = `${[environment.API_URL]}/api/todos`;
    return this.httpClient.get<Todo[]>(url);
  }
}
