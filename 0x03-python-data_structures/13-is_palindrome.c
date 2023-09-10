#include "lists.h"

/**
 * rev_lis - reverse  linked_list
 * @h: pointering to first node of list
 *
 * Return: pointer to first node in a new_list
 */
void rev_lis(listint_t **h)
{
	listint_t *pre = NULL;
	listint_t *cur = *h;
	listint_t *nxt = NULL;

	while (cur)
	{
		nxt = cur->next;
		cur->next = pre;
		pre = cur;
		cur = nxt;
	}

	*h = pre;
}

/**
 * is_palindrome - check if a linked_list is a palindrome one
 * @head: double_pointer to a linked_list
 *
 * Return: one if it's, zero if no
 */
int is_palindrome(listint_t **head)
{
	listint_t *slw = *head, *fst = *head, *tmp = *head, *dp = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fst = fst->next->next;
		if (!fst)
		{
			dp = slw->next;
			break;
		}
		if (!fst->next)
		{
			dp = slw->next->next;
			break;
		}
		slw = slw->next;
	}

	rev_lis(&dp);

	while (dp && tmp)
	{
		if (tmp->n == dp->n)
		{
			dp = dp->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}

	if (!dp)
		return (1);

	return (0);
}
