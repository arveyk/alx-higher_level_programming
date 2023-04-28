#include "lists.h"
#include <stdio.h>
#include <stdib.h>

int is_palindrome(listint_t **head)
{

	listint_t *curr = *(head);
	listint_t *other = *(head);
	int n = 0, p = 0;

	listint_t *new = *(head);
	new = (listint_t *)malloc(sizeof(listint));
	if (!new)
		return (NULL);

	if (**head != NULL)
	{
		print_listint(*head);
	}

	while (new->next != NULL)
	{
		new = new->next
		n++;
	}

	curr = new;


	print_listint(*head);
	for (n = 0; curr != *(head); n++)
	{
	
		printf("%d\n", curr->n);
		curr = curr->next;
		other = other->next;
		if (curr->n == other->n)
			p++
	}


}
