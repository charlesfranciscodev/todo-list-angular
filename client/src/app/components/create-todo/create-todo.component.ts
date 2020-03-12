import { Component, OnInit, EventEmitter, Output} from "@angular/core";
import { UserService } from "../../services/user.service";

import { User } from "../../models/User";

@Component({
  selector: "app-create-todo",
  templateUrl: "./create-todo.component.html",
  styleUrls: ["./create-todo.component.css"]
})
export class CreateTodoComponent implements OnInit {
  @Output() createTodo: EventEmitter<any> = new EventEmitter();

  title:string;
  content:string;
  completed:boolean = false;
  dueDate:string;
  priority:number = 3;
  user:User;

  users:User[];

  constructor(private userService:UserService) {}

  ngOnInit(): void {
    this.userService.getUsers().subscribe(users => this.users = users);
  }

  onSubmit() {
    let data = {
      title: this.title,
      content: this.content,
      completed: this.completed,
      dueDate: this.dueDate,
      priority: this.priority,
      user: this.user
    };

    this.createTodo.emit(data);
  }
}
