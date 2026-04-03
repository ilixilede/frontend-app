// types.ts

export interface User {
  id: string;
  name: string;
  email: string;
  role: 'admin' | 'user' | 'guest';
  createdAt: Date;
  updatedAt: Date;
}

export interface ApiResponse<T> {
  data: T;
  message: string;
  success: boolean;
  statusCode: number;
}

export type PaginationParams = {
  page: number;
  limit: number;
  sortBy?: string;
  sortOrder?: 'asc' | 'desc';
};

export interface PaginatedResponse<T> {
  items: T[];
  total: number;
  page: number;
  limit: number;
  hasNextPage: boolean;
}

export type Theme = 'light' | 'dark' | 'system';

export interface AppConfig {
  apiBaseUrl: string;
  theme: Theme;
  featureFlags: {
    enableAnalytics: boolean;
    enableNotifications: boolean;
  };
}

export type ErrorResponse = {
  error: string;
  message: string;
  statusCode: number;
  timestamp: string;
};

export type Nullable<T> = T | null;