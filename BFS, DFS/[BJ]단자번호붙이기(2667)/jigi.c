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

#define list_last_entry(ptr, type, member) \
	list_entry((ptr)->prev, type, member)

#define list_for_each_entry(pos, head, member) \
	for (pos = list_first_entry(head, typeof(*pos), member); \
	     &pos->member != (head); \
	     pos = list_next_entry(pos, member))

struct apt {
	int num;
	struct list_head list;
};

static inline void apt_list_add(struct list_head *list, int num)
{
	struct apt *iter, *apt = malloc(sizeof(struct apt));

	apt->num = num;

	list_for_each_entry(iter, list, list) {
		if (num <= iter->num)
			break;
	}

	list_add_tail(&(apt->list), &iter->list);
}

struct coord {
	short x, y;
	struct list_head list;
};

static inline void coord_list_add(struct list_head *list, short x, short y)
{
	struct coord *coord = malloc(sizeof(struct coord));

	coord->x = x;
	coord->y = y;

	list_add_tail(&(coord->list), list);
}

unsigned int size;
char **map;

static inline int in_map(unsigned short x, unsigned short y)
{
	return y < size && x < size;
}

static unsigned int explore_apt(int x, int y)
{
	static const struct coord iter_delta[4] = {
		{ .y = -1, .x =  0 }, // top
		{ .y =  1, .x =  0 }, // bottom
		{ .y =  0, .x = -1 }, // left
		{ .y =  0, .x =  1 }, // right
	};

	struct list_head houses = list_head_init(houses);
	struct coord *house;
	int d, num = 0;

	coord_list_add(&houses, x, y);
	--map[y][x];

	/*
	 * Get houses in same apartment. One apartment is a set of the houses
	 * gathered top, bottom, left and right.
	 */
	while (!list_empty(&houses)) {
		house = list_first_entry(&houses, struct coord, list);
		++num;

		for (d = 0; d < 4; d++) {
			x = house->x + iter_delta[d].x;
			y = house->y + iter_delta[d].y;

			if (in_map(x, y) && map[y][x] == '1') {
				coord_list_add(&houses, x, y);
				--map[y][x];
			}
		}

		list_del(&house->list);
		free(house);
	}

	return num;
}

int main(void)
{
	struct list_head apts = list_head_init(apts);
	struct apt *apt;
	unsigned int x, y, nr_apts = 0;

	scanf("%u", &size);

	map = malloc(sizeof(char *) * size);

	for (y = 0; y < size; y++) {
		map[y] = malloc(sizeof(char) * (size+1));
		scanf("%s\n", map[y]);
	}

	/*
	 * Explore whole map. If there is a house on the space now looking at,
	 * explore the apartment to which that house belongs.
	 */
	for (y = 0; y < size; y++) {
		for (x = 0; x < size; x++) {
			if (map[y][x] != '1')
				continue;

			apt_list_add(&apts, explore_apt(x, y));
			++nr_apts;
		}
	}

	/*
	 * Print out the number of apartments and the number of houses for each.
	 * Because the list of apartments is already sorted, all we need to do
	 * is just to pop out an apartment, print the number of houses and free.
	 */
	printf("%d\n", nr_apts);

	while (!list_empty(&apts)) {
		apt = list_first_entry(&apts, struct apt, list);

		printf("%d\n", apt->num);

		list_del(&apt->list);
		free(apt);
	}

	return 0;
}
