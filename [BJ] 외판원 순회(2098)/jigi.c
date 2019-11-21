#include <stdio.h>
#include <stdlib.h>

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

struct list_head travel = list_head_init(travel);
unsigned int **map, **min_cost, nr_city;

struct status {
	unsigned short city, visited;
	struct list_head list;
};

static inline void status_list_add(struct list_head *list, unsigned short city,
		unsigned short visited)
{
	struct status *status = malloc(sizeof(struct status));

	status->city = city;
	status->visited = visited;

	list_add_tail(&(status->list), list);
}

static void map_init(void)
{
	unsigned int i, j;

	scanf("%u\n", &nr_city);

	min_cost = malloc(sizeof(unsigned int *) * nr_city);
	map = malloc(sizeof(unsigned int *) * nr_city);

	for (i = 0; i < nr_city; i++) {
		min_cost[i] = calloc(1 << (nr_city-1), sizeof(unsigned int));
		map[i] = malloc(sizeof(unsigned int) * nr_city);

		scanf("%u", &map[i][0]);

		if (map[i][0]) {
			min_cost[i][1<<(i-1)] = map[i][0];
			status_list_add(&travel, i, 1<<(i-1));
		}
	}

	for (i = 1; i < nr_city; i++) {
		for (j = 0; j < nr_city; j++)
			scanf("%u", &map[j][i]);
	}
}

static unsigned int travel_map(void)
{
	struct status *cur;

	unsigned short visited_all = (1 << (nr_city-1)) - 1;
	unsigned int total = (unsigned int) -1;
	unsigned int i;

	while (!list_empty(&travel)) {
		cur = list_first_entry(&travel, struct status, list);

		for (i = 1; i < nr_city; i++) {
			unsigned int cost, visited;

			if (((cur->visited >> (i-1)) & 1) || !map[i][cur->city])
				continue;

			cost = min_cost[cur->city][cur->visited] + map[i][cur->city];
			visited = cur->visited | (1 << (i-1));

			if (!min_cost[i][visited] || min_cost[i][visited] > cost) {
				status_list_add(&travel, i, visited);
				min_cost[i][visited] = cost;
			}
		}

		list_del(&cur->list);
		free(cur);
	}

	for (i = 1; i < nr_city; i++) {
		if (map[0][i] && min_cost[i][visited_all]) {
			unsigned int cost = map[0][i] + min_cost[i][visited_all];

			if (total > cost)
				total = cost;
		}
	}

	return total;
}

int main(void)
{
	map_init();
	printf("%u\n", travel_map());

	return 0;
}
