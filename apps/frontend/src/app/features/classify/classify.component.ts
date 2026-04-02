import { ChangeDetectionStrategy, Component, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { finalize } from 'rxjs';
import { ApiService, ClassifyResponse } from '../../core/api.service';
import { ResultComponent } from '../result/result.component';

export interface ClassificationHistoryItem {
  text: string;
  label: string;
  confidence: number;
  createdAt: string;
}

const HISTORY_STORAGE_KEY = 'classification-history';

@Component({
  selector: 'app-classify',
  imports: [ResultComponent, RouterLink],
  templateUrl: './classify.component.html',
  styleUrl: './classify.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ClassifyComponent {
  readonly loading = signal(false);
  readonly error = signal<string | null>(null);
  readonly result = signal<ClassifyResponse | null>(null);
  readonly history = signal<ClassificationHistoryItem[]>(this.loadHistory());

  text = '';

  constructor(private readonly api: ApiService) {}

  onSubmit(): void {
    const trimmed = this.text.trim();
    if (!trimmed || this.loading()) {
      return;
    }

    this.loading.set(true);
    this.error.set(null);

    this.api
      .classify({ text: trimmed })
      .pipe(finalize(() => this.loading.set(false)))
      .subscribe({
        next: (response) => {
          this.result.set(response);

          const updatedHistory: ClassificationHistoryItem[] = [
            {
              text: trimmed,
              label: response.label,
              confidence: response.confidence,
              createdAt: new Date().toISOString()
            },
            ...this.history()
          ].slice(0, 20);

          this.history.set(updatedHistory);
          localStorage.setItem(HISTORY_STORAGE_KEY, JSON.stringify(updatedHistory));
        },
        error: () => {
          this.error.set('Unable to classify text right now. Please try again.');
        }
      });
  }

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
