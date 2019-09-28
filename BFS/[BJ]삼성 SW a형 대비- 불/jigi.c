#include <stdio.h>
#include <stdlib.h>

#ifndef typeof
#define typeof __typeof__
#endif

struct list_head {
	struct list_head *prev, *next;
};

static inline struct list_head *list_head_init(void)
{
	struct list_head *list_head = malloc(sizeof(struct list_head));

	list_head->prev = list_head;
	list_head->next = list_head;

	return list_head;
}

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

struct coord {
	short x, y;
	struct list_head list;
};

static inline void coord_list_add(struct list_head *list, int x, int y)
{
	struct coord *coord = malloc(sizeof(struct coord));

	coord->x = x;
	coord->y = y;

	list_add_tail(&(coord->list), list);
}

static inline void coord_list_free(struct list_head *list)
{
	struct coord *coord;

	while (!list_empty(list)) {
		coord = list_first_entry(list, struct coord, list);
		list_del(&coord->list);
		free(coord);
	}

	free(list);
}

struct room {
	unsigned short width, height;
	char **map;
	struct list_head *flame, *player;
};

struct room room = { 0, 0, NULL, NULL, NULL };

static void room_init(void)
{
	char *line;
	short x, y;

	room.flame = list_head_init();
	room.player = list_head_init();

	scanf("%hu %hu", &room.width, &room.height);

	room.map = malloc(sizeof(int *) * room.height);
	line = malloc(sizeof(char) * room.width+1);

	for (y = 0; y < room.height; y++) {
		room.map[y] = calloc(room.width, sizeof(int));
		scanf("%s\n", line);

		for (x = 0; x < room.width; x++) {
			struct list_head *list = room.flame;

			switch(line[x]) {
			case '@': // initial position of the player
				list = room.player;
			case '*': // initial position of flame
				coord_list_add(list, x, y);
			case '#': // the wall
				room.map[y][x] = 1;
			}
		}
	}

	free(line);
}

static void room_free(void)
{
	short y;

	for (y = 0; y < room.height; y++)
		free(room.map[y]);

	free(room.map);

	coord_list_free(room.flame);
	coord_list_free(room.player);
}

static inline int in_room(unsigned short x, unsigned short y)
{
	return y < room.height && x < room.width;
}

static inline int dead_end(unsigned short x, unsigned short y)
{
	return room.map[y][x];
}

static int escape_room(void)
{
	static const struct coord coord_delta[4] = {
		{ .x =  0, .y = -1 }, // top
		{ .x =  0, .y =  1 }, // bottom
		{ .x = -1, .y =  0 }, // left
		{ .x =  1, .y =  0 }, // right
	};

	struct list_head *next_flame, *next_player;
	int step = 1, ret = 0;

	/*
	 * Initialize the map of room, position of flames and the player.
	 */
	room_init();

	do {
		struct coord *coord;
		short x, y, d;

		next_flame = list_head_init();

		/*
		 * Get next possible positions of flame. The flame can spread
		 * top, bottom, left and right iff there are no other flames or
		 * walls. Also iff it still is in the map, for sure.
		 */
		list_for_each_entry(coord, room.flame, list) {
			for (d = 0; d < 4; d++) {
				x = coord->x + coord_delta[d].x;
				y = coord->y + coord_delta[d].y;

				if (in_room(x, y) && !dead_end(x, y)) {
					coord_list_add(next_flame, x, y);
					room.map[y][x] = 1;
				}
			}
		}

		coord_list_free(room.flame);
		room.flame = next_flame;

		/*
		 * Get next possible positions of player. The player can move to
		 * top, bottom, left and right iff there are no flames or walls
		 * on the space.
		 */
		next_player = list_head_init();

		list_for_each_entry(coord, room.player, list) {
			for (d = 0; d < 4; d++) {
				x = coord->x + coord_delta[d].x;
				y = coord->y + coord_delta[d].y;

				/*
				 * When the player reached to the outside of
				 * map, it means the player succeeded to exit.
				 */
				if (!in_room(x, y)) {
					coord_list_free(next_player);
					ret = step;
					goto out;
				}

				if (!dead_end(x, y)) {
					coord_list_add(next_player, x, y);
					room.map[y][x] = 1;
				}
			}
		}

		coord_list_free(room.player);
		room.player = next_player;

		++step;

		/*
		 * The loop of getting next positions of flame and the player,
		 * is continued until there are no ways for player to go.
		 */
	} while(!list_empty(room.player));

out:
	room_free();
	return ret;
}

int main(void)
{
	unsigned int nr_case;

	scanf("%u", &nr_case);

	for ( ; nr_case; --nr_case) {
		int step = escape_room();

		if (step)
			printf("%d\n", step);
		else
			printf("IMPOSSIBLE\n");
	}

	return 0;
}
