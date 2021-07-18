// lz78.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <queue>
#include "tree.cpp"

int main() {
	// TreeNode instantiation
	TreeNode* nodeA = new TreeNode("A"); TreeNode* nodeB = new TreeNode("B");
	TreeNode* nodeC = new TreeNode("C"); TreeNode* nodeD = new TreeNode("D");
	TreeNode* nodeE = new TreeNode("E"); TreeNode* nodeF = new TreeNode("F");
	TreeNode* nodeG = new TreeNode("G"); TreeNode* nodeH = new TreeNode("H");
	TreeNode* nodeI = new TreeNode("I");

	// construct the Binary Tree
	nodeA->leftchild = nodeB; nodeA->rightchild = nodeC;
	nodeB->leftchild = nodeD; nodeB->rightchild = nodeE;
	nodeE->leftchild = nodeG; nodeE->rightchild = nodeH;
	nodeC->leftchild = nodeF; nodeF->rightchild = nodeI;

	BinaryTree T(nodeA);

	//T.Preorder(T.root);
	//std::cout << std::endl;
	//T.Inorder(T.root);
	//std::cout << std::endl;
	//T.Postorder(T.root);
	//std::cout << std::endl;
	//T.Levelorder();
	//std::cout << std::endl;

	return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
