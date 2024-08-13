//E-ZONE MANAGER - Programme C

/**
 * @file main.c
 * @brief E-ZONE MANAGER\n\n
          Partie du projet codée en C, dont le rôle est de sélectionner certains produits parmi le catalogue d'expédition
          afin de maximiser le profit réalisé par notre camion le plus rapide.\n\n
          Références pour le C :\n
            - Quelques forums nous ont aiguillé vers les fonctions **fgets** et **strtok** afin de lire le fichier en entrée.\n
            - Les articles de **Wikipédia** et **Interstices.info** sur le problème du sac à dos nous ont aidé à comprendre
              ce problème et ses différentes méthodes de résolution.\n
            - La vidéo Youtube d'**Eric Peronnin** (Documenter un programme écrit en C avec Doxygen. Exemple avec CodeBlocks) sur le fonctionnement de
              Doxygen nous a été fort utile pour la documentation.
 *
 * @author Enguerrand LUCAT et Etienne VEYRADIER
 * @version 1.0
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/** @brief Structure permettant de stocker les informations relatives à un produit.
 *
 * @param UID   Un numéro qui permet d'identifier le produit.
 * @param prix  Le prix du produit (sa valeur marchande).
 * @param poids Le poids du produit.
 * @param nb    Le nombre de commandes du produit.
 */
typedef struct
{
    int UID;
    float prix;
    float poids;
    int nb;
} produit;


/** @brief Vérifie que le fichier à lire est disponible, c'est-à-dire qu'il est présent dans le même dossier que le fichier **main.c**.
 *
 * @return 0 si le fichier n'est pas disponible, 1 si il l'est.
 *
 */
int verif_fichier()
{
    FILE* ptr_in;
    char name[20] = {'p','r','o','d','_','l','i','v','r','a','i','s','o','n','.','c','s','v'};
    ptr_in = fopen(name, "r");
    if(!ptr_in)
    {
        return 0;
    }
    return 1;
}

/** @brief Détermine le nombre de références produits présentes dans le catalogue d'expédition
 *
 * @return La taille ainsi déterminée, une valeur entière.
 *
 */
int compteur_taille()
{
    FILE* ptr_in;
    int c;
    int taille = 0;
    char name[20] = {'p','r','o','d','_','l','i','v','r','a','i','s','o','n','.','c','s','v'};
    ptr_in = fopen(name, "r");
    while((c = fgetc (ptr_in)) != EOF)
    {
        if(c == '\n')
        {
            taille++;
        }
    }
    return taille;
}

/** @brief Lis le fichier du catalogue d'expédition et stocke celui-ci dans un tableau.
 *
 * @param[in] taille  La taille du tableau à allouer, déterminée par la fonction **compteur_taille**
 *
 * @return Le tableau de structures contenant tous les produits.
 */
produit* lecture_commande(int taille)
{
    FILE* ptr_in;
    char mystring[20];
    char * pch;
    int j = 0, i = 0;
    produit* tab;
    tab = (produit*)calloc(taille, sizeof(produit));
    char name[20] = {'p','r','o','d','_','l','i','v','r','a','i','s','o','n','.','c','s','v'};
    ptr_in = fopen(name, "r");
    if (ptr_in == NULL) perror ("Error opening file");
    else
    {
        fgets (mystring , 20 , ptr_in);
        while(fgets (mystring , 20 , ptr_in) != NULL)
        {
            j = 0;
            pch = strtok(mystring, ",");
            while (pch != NULL)
            {
                if(j == 0) tab[i].UID = atoi(pch);
                if(j == 1) tab[i].prix = atof(pch);
                if(j == 2) tab[i].poids = atof(pch);
                if(j == 3) tab[i].nb = atoi(pch);
                pch = strtok(NULL, ",");
                j++;
            }
            i++;
        }
        fclose (ptr_in);
    }
    return tab;
}

/** @brief Ecrit les UID des produits à prendre dans un fichier destiné à être lu par le Python.
 *
 * @param[in] tab  Le tableau contenant les UID des produits à prendre.
 *
 */
void export_UID(int* tab)
{
    int j = 0;
    FILE* ptr_out;
    char name[20] = {'l','i','v','r','a','i','s','o','n','_','c','a','m','i','o','n','.','t','x','t'};
    ptr_out = fopen(name, "w+");
    while(tab[j] != 0)
    {
        fprintf(ptr_out, "%d\n", tab[j]);
        j++;
    }
    fclose(ptr_out);
    printf("\n  - Données exportées");
}

/** @brief Trie les produits dans l'ordre décroissant selon leur rapport **prix/poids**.
 *
 * @param[in] N  La taille du tableau contenant les produits.
 * @param tab    Pointeur sur le tableau à trier.
 */
void triglouton(produit* tab, int N)
{
    int i,j;
    produit inter;
    for(j=1;j<=N;j++)
    {
        for(i=0;i<N-1;i++)
        {
            if( (tab[i].prix)/(tab[i].poids) < (tab[i+1].prix)/(tab[i+1].poids) )
            {
                inter = tab[i];
                tab[i] = tab[i+1];
                tab[i+1] = inter;
            }
        }
    }
}

/** @brief Trie les produits dans l'ordre décroissant selon leur **prix**.
 *
 * @param[in] N  La taille du tableau contenant les produits.
 * @param tab    Pointeur sur le tableau à trier.
 */
void tribrut(produit* tab, int N)
{
    int i,j;
    produit inter;
    for(j=1;j<=N;j++)
    {
        for(i=0;i<N-1;i++)
        {
            if( (tab[i].prix) < (tab[i+1].prix) )
            {
                inter = tab[i];
                tab[i] = tab[i+1];
                tab[i+1] = inter;
            }
        }
    }
}

/** @brief Détermine les produits à prendre selon la méthode **gloutonne**.
 *
 * @param[in] tab  Le tableau contenant les produits.
 * @param[in] N    La taille du tableau.
 * @param[in] plim La capacité (poids limite) du camion à charger.
 *
 * @return Un tableau contenant les UID des produits à prendre.
 */
int* glouton(produit* tab, int N, float plim)
{
    int i = 0, j = 0, taille = 0, i1;
    float ptot = 0;
    for(i1 = 0; i1 < N-1; i1++)
    {
        taille = taille + tab[i1].nb;
    }
    int* tabglouton;
    tabglouton = (int*)calloc(taille, sizeof(int));
    triglouton(tab, N);
    while((ptot < plim) && (i < N))
    {
        while((tab[i].nb > 0) && (ptot + tab[i].poids <= plim))
        {
            tabglouton[j] = tab[i].UID;
            tab[i].nb = tab[i].nb - 1;
            ptot = ptot + tab[i].poids;
            j++;
        }
        i++;
    }
    return tabglouton;
}

/** @brief Renvoie la valeur maximale du chargement obtenue en utilisant la méthode **gloutonne**.
 *
 * @param[in] tab  Le tableau contenant les produits.
 * @param[in] N    La taille du tableau.
 * @param[in] plim La capacité (poids limite) du camion à charger.
 *
 * @return La valeur **vtot** obtenue.
 */
float testglouton(produit* tab, int N, float plim)
{
    int i = 0;
    float ptot = 0, vtot = 0;
    triglouton(tab, N);
    while((ptot < plim) && (i < N))
    {
        while((tab[i].nb > 0) && (ptot + tab[i].poids <= plim))
        {
            tab[i].nb = tab[i].nb - 1;
            ptot = ptot + tab[i].poids;
            vtot = vtot + tab[i].prix;
        }
        i++;
    }
    return vtot;
}

/** @brief Détermine les produits à prendre selon la méthode de la **force brute**.
 *
 * @param[in] tab  Le tableau contenant les produits.
 * @param[in] N    La taille du tableau.
 * @param[in] plim La capacité (poids limite) du camion à charger.
 *
 * @return Un tableau contenant les UID des produits à prendre.
 */
int* forcebrute(produit* tab, int N, float plim)
{
    int i = 0, j = 0, taille = 0, i1;
    float ptot = 0;
    for(i1 = 0; i1 < N; i1++)
    {
        taille = taille + tab[i1].nb;
    }
    int* tabbrut;
    tabbrut = (int*)calloc(taille, sizeof(int));
    tribrut(tab, N);
    while((ptot < plim) && (i < N))
    {
        while((tab[i].nb > 0) && (ptot + tab[i].poids <= plim))
        {
            tabbrut[j] = tab[i].UID;
            tab[i].nb = tab[i].nb - 1;
            ptot = ptot + tab[i].poids;
            j++;
        }
        i++;
    }
    return tabbrut;
}

/** @brief Renvoie la valeur maximale du chargement obtenue en utilisant la méthode de la **force brute**.
 *
 * @param[in] tab  Le tableau contenant les produits.
 * @param[in] N    La taille du tableau.
 * @param[in] plim La capacité (poids limite) du camion à charger.
 *
 * @return La valeur **vtot** obtenue.
 */
float testbrut(produit* tab, int N, float plim)
{
    int i = 0;
    float ptot = 0, vtot = 0;
    tribrut(tab, N);
    while((ptot < plim) && (i < N))
    {
        while((tab[i].nb > 0) && (ptot + tab[i].poids <= plim))
        {
            tab[i].nb = tab[i].nb - 1;
            ptot = ptot + tab[i].poids;
            vtot = vtot + tab[i].prix;
        }
        i++;
    }
    return vtot;
}

/** @brief Résout le 'problème du sac à dos' en choississant la méthode à utiliser selon les valeurs obtenues par les fonctions test,
           et exporte ensuite les valeurs des UID à prendre grâce à la fonction **export_UID**.

           EDIT : Cette fonction n'appelle finalement que la méthode gloutonne car la comparaison des deux méthodes mène dans certains
           cas à une erreur que nous n'avons pas réussi à résoudre.
           Nous sommes désolés de ce dysfonctionnement, le code complet est toujours apparent en commentaires dans la fonction.
 *
 * @param[in] tab  Le tableau contenant les produits.
 * @param[in] N    La taille du tableau.
 * @param[in] plim La capacité (poids limite) du camion à charger.
 *
 */
void sacados(produit* tab, int N, float plim)
{
    int i, taille;
    float pglouton, pbrut;
    for(i = 0; i < N; i++)
    {
        taille = taille + tab[i].nb;
    }
    int* tabuid;
    tabuid = (int*)calloc(taille, sizeof(int));
    /*pglouton = testglouton(tab, N, plim);
    pbrut = testbrut(tab, N, plim);
    if(pglouton >= pbrut)
    {
        tabuid = glouton(tab, N, plim);
    }
    else
    {
        tabuid = forcebrute(tab, N, plim);
    }*/
    tabuid = glouton(tab, N, plim);
    printf("\n  - Optimisation terminée");
    export_UID(tabuid);
}

/** @brief Fonction main : Affiche les étapes du processus et appelle les différentes fonctions.
 *
 * @return 0, comme tout bon int main().
 */
int main()
{
    printf("Bonjour, bienvenue dans le programme d'optimisation du chargement\n");

    // Déclaration des variables
    int test, taille;
    float capacite;
    produit* tab;

    // Définition de la capacité du camion
    printf("Saisir la capacité du camion : ");
    scanf("%f", &capacite);

    // Paramétrage de la console pour avoir les accents (codage UTF-8)
    system("chcp 65001");

    // Vérification de la disponibilité du fichier
    test = verif_fichier();
    if(test == 0)
    {
        printf("\nErreur : le fichier n'est pas reconnu");
        return 0;
    }
    printf("\n  - Fichier lu");

    // Affectation de la taille
    taille = compteur_taille();
    // Remplissage du tableau de produits
    tab = lecture_commande(taille);
    // Résolution du problème d'optimisation
    sacados(tab, taille, capacite);
    printf("\n\nVeuillez retourner sur Python pour consulter les résultats\n\nBonne journée !\n");
    return 0;
}
