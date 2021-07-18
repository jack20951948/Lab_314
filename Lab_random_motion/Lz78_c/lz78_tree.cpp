#include<iostream> 
#include<stdlib.h>
bool debug = false;

struct binary_search_tree_node
{
	int data;
	struct binary_search_tree_node* father;
	struct binary_search_tree_node* children[7];
};
typedef struct binary_search_tree_node BSTNode;

void print_inorder(BSTNode *ptr);
BSTNode *init_root(BSTNode *root);
BSTNode *insert_node(BSTNode *root, int value);
BSTNode *find_node(BSTNode *ptr, int value);

int main()
{
    int data[] = {10, 20, 5, 8, 30, 15, 1, 18};
    int ndata = sizeof(data)/sizeof(int);
    BSTNode *root = 0;

    for (int i=0; i<ndata; i++)
        root = insert_node(root, data[i]);

    assert(find_node(root, 15));

    assert(!find_node(root, 11));

    system("pause");
    return 0;
}

BSTNode *init_root(BSTNode *root)
{
    BSTNode *root_node;
    if (root == 0)
    {
        root_node = (BSTNode *) malloc(sizeof(BSTNode));
        root_node->data = 7;
        root_node->father = 0;
        for(int i=0 ; i<7 ; i++)
        {
            BSTNode* newNode = (BSTNode *) malloc(sizeof(BSTNode));
            root_node->children[i] = newNode;
        }

        return root_node;
    }
    else
    {
        return root;
    }
}

// 插入節點
BSTNode *insert_node(BSTNode *root, int value)
{
    BSTNode *new_node;
    BSTNode *current;
    BSTNode *parent;

    // 建立節點
    new_node = (BSTNode *) malloc(sizeof(BSTNode));
    new_node->data = value;
    new_node->left = 0;
    new_node->right = 0;
    if (root == 0)    // 目前無資料
    {
        return new_node;
    }
    else
    {
        current = root; // 從頭找要新節點之插入點
        while (current != 0)
        {
            parent = current;       // 找新節點之父節點
            if (current->data > value)
                current = current->left;    // 往左找
            else
                current = current->right;   // 往右找
        }
        if (parent->data > value)    // 插入此父節點左邊或右邊
            parent->left = new_node;
        else
            parent->right = new_node;
    }
    return root;    // 回傳此樹
}

