import { ChangeDetectionStrategy, Component, input } from '@angular/core';
import { PercentPipe } from '@angular/common';
import { ClassifyResponse } from '../../core/api.service';

@Component({
  selector: 'app-result',
  imports: [PercentPipe],
  templateUrl: './result.component.html',
  styleUrl: './result.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ResultComponent {
  readonly result = input<ClassifyResponse | null>(null);
}
