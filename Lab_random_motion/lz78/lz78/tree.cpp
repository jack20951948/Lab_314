#include <string>

class BinaryTree;
class TreeNode {
public:
	TreeNode* leftchild;
	TreeNode* rightchild;
	TreeNode* parent;
	std::string str;

	TreeNode() :leftchild(0), rightchild(0), parent(0), str("") {};
	TreeNode(std::string s) :leftchild(0), rightchild(0), parent(0), str(s) {};

	friend class BinaryTree;
};
class BinaryTree {
public:
	TreeNode* root;         // 以root作為存取整棵樹的起點
	BinaryTree() :root(0) {};
	BinaryTree(TreeNode* node) :root(node) {};

	void Preorder(TreeNode* current);
	void Inorder(TreeNode* current);
	void Postorder(TreeNode* current);
	void Levelorder();
};
// definition of BinaryTree::Preorder()
// definition of BinaryTree::Inorder()
// definition of BinaryTree::Postorder()
// definition of BinaryTree::Levelorder()