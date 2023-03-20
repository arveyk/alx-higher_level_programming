#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node
 * @head: pointer to pointer to head node
 * @number: data for new node
 *
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{

	listint_t *ptr = (*head);
	listint_t *new = NULL;
	size_t r = 0;

	if (head == NULL)
		(*head) = new;

	while (r++ < 4)
		ptr = ptr->next;
	if (ptr->next == NULL)
	{
	
		ptr->next = new;
	}

	new = (listint_t *)malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = ptr->next;
	ptr->next = new;

	return (new);
}
