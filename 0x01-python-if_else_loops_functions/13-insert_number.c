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
	listint_t *ptr2 = NULL;

	if (head == NULL)
		(*head) = new;

	while (ptr->n < number)
	{
		ptr2 = ptr;
		ptr = ptr->next;
	}


	new = (listint_t *)malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = ptr2->next;
	ptr2->next = new;

	return (new);
}
