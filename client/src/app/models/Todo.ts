import { User } from './User';

export class Todo {
  todoId:number;
  title:string;
  content:string;
  completed:boolean;
  dueDate:string;
  priority:number;
  user:User;
}
