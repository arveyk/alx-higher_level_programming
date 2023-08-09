#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - inserts a node in a sorted linked list
 * @head: address of pointer to first node
 * @number: data for new node
 *
 * Return: address of new node of NULL if fails
 */
listint_t *insert_node(listint_t **head, int number)
{

	listint_t *walk = *head;
	listint_t *prev = *head;
	listint_t *new_mbr;

	new_mbr = malloc(sizeof(listint_t));
	if (new_mbr == NULL)
		return (NULL);

	new_mbr->n = number;
	if (*head == NULL)
	{
		*head = new_mbr;
		new_mbr->next = NULL;
		return (new_mbr);
	}
	if (number < prev->n)
	{
		new_mbr->next = *head;
		*head = new_mbr;
		return (new_mbr);
	}
	else
		while (walk->next != NULL)
		{
			if (walk->n > number)
				break;
			prev = walk;
			walk = walk->next;
		}
	if (number > walk->n)
	{
		new_mbr->next = walk->next;
		walk->next = new_mbr;
	}
	else
	{
		new_mbr->next = prev->next;
		prev->next = new_mbr;
	}
	return (new_mbr);
}
