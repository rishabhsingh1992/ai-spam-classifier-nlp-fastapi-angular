import { Routes } from '@angular/router';
import { ClassifyComponent } from './features/classify/classify.component';
import { HistoryComponent } from './features/history/history.component';

export const routes: Routes = [
  {
    path: '',
    component: ClassifyComponent
  },
  {
    path: 'history',
    component: HistoryComponent
  }
];
