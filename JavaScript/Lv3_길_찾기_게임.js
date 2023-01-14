class BinaryTree {
  constructor(val, x) {
    this.val = val;
    this.x = x;
    this.left = null;
    this.right = null;
  }

  insert(val, x) {
    this.x >= x ? this.toLeft(val, x) : this.toRight(val, x);
  }

  toLeft(val, x) {
    this.left ? this.left.insert(val, x) : (this.left = new BinaryTree(val, x));
  }

  toRight(val, x) {
    this.right
      ? this.right.insert(val, x)
      : (this.right = new BinaryTree(val, x));
  }
}

const preorder = (bTree, arr) => {
  if (bTree !== null) {
    arr.push(bTree.val);
    preorder(bTree.left, arr);
    preorder(bTree.right, arr);
  }
};

const postorder = (bTree, arr) => {
  if (bTree !== null) {
    postorder(bTree.left, arr);
    postorder(bTree.right, arr);
    arr.push(bTree.val);
  }
};

function solution(nodeinfo) {
  const preorderArr = [];
  const postorderArr = [];

  const nodes = nodeinfo
    .map((node, idx) => [idx + 1, ...node])
    .sort((a, b) => b[2] - a[2]);

  const bTree = new BinaryTree(nodes[0][0], nodes[0][1]);
  for (let i = 1; i < nodes.length; i++) bTree.insert(nodes[i][0], nodes[i][1]);

  preorder(bTree, preorderArr);
  postorder(bTree, postorderArr);

  return [preorderArr, postorderArr];
}
