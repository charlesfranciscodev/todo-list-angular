import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { environment } from "src/environments/environment";

import { Todo } from "../models/Todo";
import { Observable } from "rxjs";

const httpOptions = {
  headers: new HttpHeaders({
    "Content-Type": "application/json"
  })
};

@Injectable({
  providedIn: "root"
})
export class TodoService {
  constructor(private httpClient:HttpClient) {}

  getTodos():Observable<Todo[]> {
    const url = `${[environment.API_URL]}/api/todos`;
    return this.httpClient.get<Todo[]>(url);
  }

  deleteTodo(todo:Todo):Observable<any> {
    const url = `${[environment.API_URL]}/api/todos/${todo.todoId}`;
    return this.httpClient.delete<any>(url);
  }

  createTodo(body:any):Observable<any> {
    const url = `${[environment.API_URL]}/api/todos`;
    return this.httpClient.post<any>(url, body, httpOptions);
  }
}
