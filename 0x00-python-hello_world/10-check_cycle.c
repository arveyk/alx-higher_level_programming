#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks for the existance of a cycle in a listint_t list
 * @list: pointer to head node
 *
 * Return: 0 if no cycle, 1 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *trav = NULL;
	listint_t *comp = NULL;

	if (list == NULL)
		return (0);
	trav = list->next;
	while (trav != NULL)
	{
		if (trav == list)
			return (1);
		comp = trav->next;
		while (comp != NULL)
		{
			if (comp == trav)
				return (1);
			comp = comp->next;
		}
		trav = trav->next;
	}
	return (0);
}
