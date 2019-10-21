#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#ifndef typeof
#define typeof __typeof__
#endif

struct list_head {
	struct list_head *prev, *next;
};

#define list_head_init(head) { &(head), &(head) }

static inline int list_empty(const struct list_head *head)
{
	return head->next == head;
}

static inline void __list_add(struct list_head *new, struct list_head *prev,
		struct list_head *next)
{
	next->prev = new;
	new->next = next;
	new->prev = prev;
	prev->next = new;
}

static inline void list_add_tail(struct list_head *new, struct list_head *head)
{
	__list_add(new, head->prev, head);
}

static inline void __list_del(struct list_head * prev, struct list_head * next)
{
	next->prev = prev;
	prev->next = next;
}

static inline void __list_del_entry(struct list_head *entry)
{
	__list_del(entry->prev, entry->next);
}

static inline void list_del(struct list_head *entry)
{
	__list_del_entry(entry);
	entry->next = NULL;
	entry->prev = NULL;
}

#define offsetof(type, member) ((size_t)&((type *)0)->member)

#define container_of(ptr, type, member) ({ \
	void *__mptr = (void *)(ptr); \
	((type *)(__mptr - offsetof(type, member))); })

#define list_entry(ptr, type, member) \
	container_of(ptr, type, member)

#define list_first_entry(ptr, type, member) \
	list_entry((ptr)->next, type, member)

#define list_next_entry(pos, member) \
	list_entry((pos)->member.next, typeof(*(pos)), member)

#define list_prev_entry(pos, member) \
	list_entry((pos)->member.prev, typeof(*(pos)), member)

#define list_last_entry(ptr, type, member) \
	list_entry((ptr)->prev, type, member)

#define list_for_each_entry(pos, head, member) \
	for (pos = list_first_entry(head, typeof(*pos), member); \
	     &pos->member != (head); \
	     pos = list_next_entry(pos, member))

#define list_for_each_entry_reverse(pos, head, member) \
	for (pos = list_last_entry(head, typeof(*pos), member); \
	     &pos->member != (head); \
	     pos = list_prev_entry(pos, member))

struct vertex {
	short id;
	struct list_head list;
};

#define vertex_of(ptr) list_entry(ptr, struct vertex, list)

static inline void vertex_list_add(struct list_head *list, int id, bool sort)
{
	struct vertex *iter, *vertex = malloc(sizeof(struct vertex));

	vertex->id = id;

	list_for_each_entry(iter, list, list) {
		if (!sort || id <= iter->id)
			break;
	}

	list_add_tail(&vertex->list, sort ? &iter->list : list);
}

struct list_head *edge_of, path = list_head_init(path);
unsigned short nr_vertex, start;
bool *visit;

static void graph_init(void)
{
	unsigned short nr_edge;
	int i;

	scanf("%hu %hu %hu", &nr_vertex, &nr_edge, &start);

	edge_of = malloc(sizeof(struct list_head) * nr_vertex);
	visit = malloc(sizeof(bool) * nr_vertex);

	for (i = 0; i < nr_vertex; i++) {
		edge_of[i].prev = edge_of[i].next = &edge_of[i];
	}

	for (i = 0; i < nr_edge; i++) {
		unsigned short va, vb;
		scanf("%hu %hu", &va, &vb);

		vertex_list_add(&edge_of[va-1], vb-1, true);
		vertex_list_add(&edge_of[vb-1], va-1, true);
	}
}

enum {
	DEPTH_FIRST = 0,
	BREADTH_FIRST,
	NR_METHODS
};

static void visit_next_vertex(struct vertex *vertex, unsigned int method)
{
	struct vertex *iter;

	if (method == DEPTH_FIRST)
		/*
		 * While the sparse matrix for the graph representation is
		 * sorted in ascending order, we need to stack those in
		 * descending order. So travel the sparse matrix reversed.
		 */
		list_for_each_entry_reverse(iter, &edge_of[vertex->id], list) {
			if (!visit[iter->id]) {
				vertex_list_add(&path, iter->id, false);
			}
		}

	else
		list_for_each_entry(iter, &edge_of[vertex->id], list) {
			if (!visit[iter->id]) {
				vertex_list_add(&path, iter->id, false);
			}
		}
}

int main(void)
{
	struct vertex *vertex;
	unsigned int method;

	/*
	 * Initialize the graph of given vertices and edges. The graph will be
	 * represented as a form of sparse matrix.
	 */
	graph_init();

	/*
	 * Travel the graph with the method of DFS and BFS, respectively. The
	 * first iteration of the loop will be done with DFS, and the second
	 * one will be done with BFS.
	 */
	for (method = 0; method < NR_METHODS; method++) {
		memset(visit, 0, sizeof(bool) * nr_vertex);
		vertex_list_add(&path, start-1, false);

		while (!list_empty(&path)) {
			vertex = (method == DEPTH_FIRST) ?
				list_last_entry(&path, struct vertex, list) :
				list_first_entry(&path, struct vertex, list);

			if (!visit[vertex->id]) {
				visit[vertex->id] = true;
				printf("%d ", vertex->id+1);

				visit_next_vertex(vertex, method);
			}

			list_del(&vertex->list);
			free(vertex);
		}

		printf("\n");
	}

	/*
	 * We have some allocated memories to be freed left, but hey, this is
	 * the end of this program. Skip freeing those allocated memory.
	 */
	return 0;
}
