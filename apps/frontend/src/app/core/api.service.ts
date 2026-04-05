import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface ClassifyRequest {
  text: string;
}

export interface ClassifyResponse {
  label: string;
  confidence: number;
}

@Injectable({ providedIn: 'root' })
export class ApiService {
  private readonly http = inject(HttpClient);

  classify(payload: ClassifyRequest): Observable<ClassifyResponse> {
    return this.http.post<ClassifyResponse>('http://127.0.0.1:8000/classify', payload);
  }
}
