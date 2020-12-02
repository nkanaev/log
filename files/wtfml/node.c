struct obj {
  enum type {
    T_NODE,
    T_ATTR,
    T_TEXT,
  };
  union {
    struct { const char* name, node* children } n;
    struct { node* pairs; } a;
    struct {} pair;
  };
};

struct node {
  void* val;
  node* next;
};
