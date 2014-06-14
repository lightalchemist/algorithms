#ifndef UNION_FIND_H
#define UNION_FIND_H

#include <vector>
#include <assert.h>


class UnionFind
{
    public:
        UnionFind(unsigned int num_elements);
        bool is_connected(unsigned int p, unsigned int q);
        void connect(unsigned int p, unsigned int q);
    private:
        std::vector<unsigned int> id;
        std::vector<unsigned int> size;
        unsigned int root(unsigned int p);
};


UnionFind::UnionFind(unsigned int num_elements)
{
    id = std::vector<unsigned int>(num_elements, 0);
    size = std::vector<unsigned int>(num_elements);
    for (int i = 0; i < id.size(); ++i)  // Init each node to be its own root.
        id[i] = i;
}


bool UnionFind::is_connected(unsigned int p, unsigned int q)
{
    return root(p) == root(q);
}


void UnionFind::connect(unsigned int p, unsigned int q)
{
    unsigned int root_p = root(p);
    unsigned int root_q = root(q);
    if (root_p != root_q)
    {
        if (size[root_p] < size[root_q])
        {
            size[root_q] += size[root_p];
            id[root_p] = root_q;  // Join to root of tree containing q
        }
        else
        {
            size[root_p] += size[root_q];
            id[root_q] = root_p;  // Join to root of tree containing p
        }
    }
}


unsigned int UnionFind::root(unsigned int p)
{
    while (p != id[p])  // Keep moving up tree until it reaches root.
    {
        id[p] = id[id[p]];  // Path compression.
        p = id[p];
    }

    return p;
}

#endif


int main(void)
{
    UnionFind uf(10000);
    uf.connect(0, 1);
    uf.connect(2, 3);
    uf.connect(4, 5);
    uf.connect(6, 7);
    uf.connect(0, 3);
    uf.connect(2, 4);
    uf.connect(7, 1);

    assert(uf.is_connected(7, 3));
    assert(uf.is_connected(2, 6));
    assert(uf.is_connected(3, 6));

    assert(!uf.is_connected(0, 10));
        
    return 0;
}
