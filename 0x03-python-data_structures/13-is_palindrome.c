#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

int is_eq(int *a, int b);
/**
 * is_palindrome - checks if a single linked list is
 * a palindrome
 * @head: pointer to pointer to first node
 *
 * Return: 0 if not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *trav = *head;
	int *list_nums;
	int counter = 0;
	int w = 0;
	int end;

	if (head == NULL || *head == NULL)
		return (0);
	while (trav != NULL)
	{
		trav = trav->next;
		counter++;
	}
	trav = *head;
	if (counter <= 3)
	{
		if (counter == 1)
			return (1);
		if (counter == 2)
		{
			if ((*head)->n == (*head)->next->n)
				return (1);
		}
		if (counter == 3)
		{
			trav = (*head)->next;
			if ((*head)->n == trav->next->n)
				return (1);
		}
		return (0);
	}
	list_nums = malloc(counter * sizeof(int));
	if (list_nums == NULL)
		return (0);
	while (trav != NULL)
	{
		list_nums[w] = trav->n;
		trav = trav->next;
		w++;
	}
	end = counter - 1;
	if (is_eq(list_nums, end) == 0)
		return (0);
	free(list_nums);
	return (1);
}

/**
 * is_eq - checks if array is apalindrome
 * @lst_ptr: pointer to malloced list to check
 * @b: second
 *
 * Return: 1 if true, 0 if not
 */
int is_eq(int *lst_ptr, int b)
{
	int begn = 0;
	int end = b;

	while (begn < end)
	{
		if (lst_ptr[begn] != lst_ptr[end])
			return (0);
		begn++;
		end--;
	}
	return (1);
}
