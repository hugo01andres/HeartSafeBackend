export type ActionWithPayload<T extends string, P> = {
  type: T;
  payload: P;
};
