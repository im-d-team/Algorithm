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

struct status {
	/*
	 * city: the city where the salesman is currently visiting.
	 * visited: the bitmap for the cities where the salesman once visited.
	 */
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

/*
 * map[a][b]: the distance to `a` from `b`.
 * cost[a][visited]: the distance to 'a' after visiting all `visited`.
 */
unsigned int **map, **cost, nr_city;
struct list_head travel = list_head_init(travel);

static void map_init(void)
{
	unsigned int i, j;

	scanf("%u\n", &nr_city);

	cost = malloc(sizeof(unsigned int *) * nr_city);
	map = malloc(sizeof(unsigned int *) * nr_city);

	for (i = 0; i < nr_city; i++) {
		/*
		 * Because the salesman starts visiting from a specific city,
		 * the bit for that city always is 1 on `visited` bitmap. So
		 * no need to represent one bit for that city.
		 */
		cost[i] = calloc(1 << (nr_city-1), sizeof(unsigned int));
		map[i] = malloc(sizeof(unsigned int) * nr_city);
	}

	for (i = 0; i < nr_city-1; i++) {
		for (j = 0; j < nr_city; j++)
			scanf("%u", &map[j][i]);
	}

	/*
	 * The salesman starts visiting from the last city. So, the distance to
	 * `j` from `i`, which is the last city, is identical with the distance
	 * to `j` after visiting `i`.
	 */
	for (j = 0; j < nr_city; j++) {
		scanf("%u", &map[j][i]);

		if (map[j][i]) {
			cost[j][1<<j] = map[j][i];
			status_list_add(&travel, j, 1 << j);
		}
	}

	--nr_city;
}

static unsigned int travel_map(void)
{
	struct status *cur;

	unsigned short visited_all = (1 << nr_city) - 1;
	unsigned int total_cost = (unsigned int) -1;
	unsigned int i;

	while (!list_empty(&travel)) {
		cur = list_first_entry(&travel, struct status, list);

		for (i = 0; i < nr_city; i++) {
			unsigned int c, v;

			/*
			 * Impossible to visit the city where the salesman once
			 * visited, or has no way to go from current city.
			 */
			if (((cur->visited >> i) & 1) || !map[i][cur->city])
				continue;

			c = cost[cur->city][cur->visited] + map[i][cur->city];
			v = cur->visited | (1 << i);

			if (!cost[i][v] || cost[i][v] > c) {
				status_list_add(&travel, i, v);
				cost[i][v] = c;
			}
		}

		list_del(&cur->list);
		free(cur);
	}

	/*
	 * The salesman visited every city and now it's time to go back to the
	 * city where the salesman started his/her travel. Find minimum total
	 * distance of traveling.
	 */
	for (i = 0; i < nr_city; i++) {
		if (map[nr_city][i] && cost[i][visited_all]) {
			unsigned int c = map[nr_city][i] + cost[i][visited_all];

			if (total_cost > c)
				total_cost = c;
		}
	}

	return total_cost;
}

int main(void)
{
	map_init();
	printf("%u\n", travel_map());

	/*
	 * We have some allocated memories to be freed left, but hey, this is
	 * the end of this program. Skip freeing those allocated memory.
	 */
	return 0;
}
