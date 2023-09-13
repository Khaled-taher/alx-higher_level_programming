#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <Python.h>

/**
 * print_python_bytes - print the python info
 * @p: pointer to python object
 * Return: return nothing
 */
void print_python_bytes(PyObject *p)
{
	long int s;
	int i;
	char *try_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &try_str, &s);

	printf("  size: %li\n", s);
	printf("  trying string: %s\n", try_str);
	if (size < 10)
		printf("  first %li bytes:", s + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= s && i < 10; i++)
		printf(" %02hhx", try_str[i]);
	printf("\n");
}

/**
 * print_python_list - print the python info
 * @p: pointer to python object
 * Return: return nothing
 * */

void print_python_list(PyObject *p)
{
        long int s = PyList_Size(p);
        int i;
        PyListObject *list = (PyListObject *)p;
        const char *ty;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", s);
        printf("[*] Allocated = %li\n", list->allocated);
        for (i = 0; i < s; i++)
        {
                ty = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, ty);
                if (!strcmp(ty, "bytes"))
                        print_python_bytes(list->ob_item[i]);
        }
}
