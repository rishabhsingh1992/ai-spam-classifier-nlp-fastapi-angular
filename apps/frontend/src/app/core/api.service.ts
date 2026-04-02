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
    return this.http.post<ClassifyResponse>('/classify', payload);
  }
}
