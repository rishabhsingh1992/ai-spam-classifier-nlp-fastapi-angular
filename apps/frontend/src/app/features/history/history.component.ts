import { ChangeDetectionStrategy, Component, signal } from '@angular/core';
import { DatePipe, PercentPipe } from '@angular/common';
import { RouterLink } from '@angular/router';
import { ClassificationHistoryItem } from '../classify/classify.component';

const HISTORY_STORAGE_KEY = 'classification-history';

@Component({
  selector: 'app-history',
  imports: [DatePipe, PercentPipe, RouterLink],
  templateUrl: './history.component.html',
  styleUrl: './history.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class HistoryComponent {
  readonly history = signal<ClassificationHistoryItem[]>(this.loadHistory());

  private loadHistory(): ClassificationHistoryItem[] {
    const raw = localStorage.getItem(HISTORY_STORAGE_KEY);
    if (!raw) {
      return [];
    }

    try {
      const parsed = JSON.parse(raw) as ClassificationHistoryItem[];
      return Array.isArray(parsed) ? parsed : [];
    } catch {
      return [];
    }
  }
}
