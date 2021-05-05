# Crypto_Math
 Tools for cryptography

Crypto_Math is program for helping with Cryptographic Math.

What can Crypto_Math do:
+ get GCD of the number
+ factorized number
+ solve Chinese Remainder Theorem
+ find inverse number for given one in Multiplicative Group
+ compute Euler function for given number
+ find multiplicative group of given Modulus
+ find orders of all elements in Multiplicative Group
+ check if given curve is elliptic
+ check if given point is on Elliptic Curve
+ add two point on Elliptic Curve
+ find order of Elliptic Curve
+ find order of given point of Elliptic Curve
+ find orders of all points of Elliptic Curve
+ compute secret of EC Diffie-Hellman by doing MOV Attack
+ get help table for Bilinear operations
+ compute Linear Congruential Generator
+ demonstrate One-bit Commitment
# USE
Program should be run from terminal by command: python3 main.py ARGUMENTS

## GCD (Greatest Common Divisor)

- find Greatest Common Divisor of two given numbers
```
Format: -g NUMBER_X,NUMBER_Y

Example: -g 15,3

Output: "GCD is 3"
```

## Factorization

- factorized given number
```
Format: -f NUMBER

Example: -f 15

Output: "       Number 15 can be factorize to: [3, 5]"
```

## Chinese Remainder Theorem (CTR)
x ≡ Y1 mod MODULUS1
x ≡ Y2 mod MODULUS2
x ≡ Y3 mod MODULUS3

- solve CTR for given equations
```
Format: -c Y1modMODULUS1,Y2modMODULUS2,...
Example: -c 5mod7,3mod5
Output:"    M: 35
            N: [5.0, 7.0]
            L: [3, 3]
            x = 33.0    "
```

## Inverse number

- find inverse number for given number in Multiplicative Group
```
Format: -i NUMBER,MODULUS

Example: -i 5,11

Output:"Inverse of number 5 is 9"
```

## Phi (Euler number)

- compute Euler number for given number
```
Format: -p NUMBER

Example: -p 11

Output:"Euler function of number 11 is 10"
```

## Multiplicative group

- find multiplicative group for given number
```
Format: --group NUMBER

Example: --group 11

Output:"Group is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
```
- find orders for multiplicative group for given number
```
Format: --orders_of_group NUMBER

Example: --orders_of_group 11

Output:"    Group is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            [1] have order 1
            [10] have order 2
            [3, 4, 5, 9] have order 5
            [2, 6, 7, 8] have order 10 -> GENERATORS!   "
```

# Elliptic Curves

- give information about curve to the program. If no other function is used, program check if given curve is elliptic or not

Example of format for equation of curve: A0* y^2 + A1 * y + A2 * y * x = A3 * x^3 + A4 * x^2 + A5 * x + A6

WARNING!!! If A0 is negative, for example -1, write instead of symbol "-" symbol"/". Example: -1 -> /1
```
Format: --curve A0,A1,A2,A3,A4,A5,A6

Example: Curve is y^2 = x^3 + 2* x + 1 -> 1* y^2 + 0 * y + 0 * y * x = 1 * x^3 + 0 * x^2 + 2 * x + 1
        --curve 1,0,0,1,0,1,1

Output:"Elliptic curve: y^2 + 0 * y + 0 * xy = x^3 + 0 * x^2 + 1 * x + 1"
```

## P_point and Q_point
- help parameter for giving program information about P (Q) point. If only P_point (Q_point) is given, no function will happen!

WARNING!!! If X is negative, for example -1, write instead of symbol "-" symbol"/". Example: -1 -> /1
```
Format: --p_point X,Y

Example:    P is [-1,-2] then write: --p_point /1,-2
            Q is [1,2] then write: --q_point 1,2Example

Output: NO OUTPUT!
```

## Field

- help parameter for giving program information about field. If only field is given, no function will happen!
```
Format: --field FIELD
Example: --field 5
Output: NO OUTPUT!
```
## Order of Elliptic curve

- function to find order for given Elliptic curve
MUST GIVEN PARAMETER!!!: curve, field
```
Format: --curve A0,A1,A2,A3,A4,A5,A6 --field FIELD --order_of_ec

Example: --curve 1,0,0,1,0,-1,-1  --field 7 --order_of_ec

Output:"    Given curve is elliptic.
            Elliptic curve: y^2 + 0 * y + 0 * xy = x^3 + 0 * x^2 - 1 * x - 1
             x  | x part | y^2 | y   | Points
             0  | 6      | -   | -   | -                  |
             1  | 6      | -   | -   | -                  |
             2  | 5      | -   | -   | -                  |
             3  | 2      | 9   | +-3 | [[3, 3], [3, -3]]  |
             4  | 3      | -   | -   | -                  |
             5  | 0      | 0   | +-0 | [[5, 0]]           |
             6  | 6      | -   | -   | -                  |
             ∞  | -      | -   | ∞   | [∞,∞]              |
            Order of E[F7] is: 4    "
```

## Check point on elliptic curve
- find if given point is on given curve or not
MUST GIVEN PARAMETER!!!: p_point, curve, field
```
Format: --p_point X,Y --curve A0,A1,A2,A3,A4,A5,A6 --field FIELD --point_on_curve

Example: --p_point 0,1 --field 7 --curve 1,0,0,1,0,2,1 --point_on_curve

Output:"        Point (0,1) is on elliptic curve!       "
```

## Adding points on EC

- function for adding two given points (P,Q) on given elliptic curve

MUST GIVEN PARAMETER!!!: p_point, q_point,curve, field
```
Format: --p_point Xp,Yp --q_point Xq,Yq --curve A0,A1,A2,A3,A4,A5,A6 --field FIELD --point_on_curve

Example: --p_point 1,2 --q_point 0,1 --field 7 --curve 1,0,0,1,0,2,1 --add_points_ec

Output:"        P =  [1, 2], Q =  [0, 1], R = P + Q =  [0, 6]   "
```

## Order of point on EC
- function for finding order for one given point

MUST GIVEN PARAMETER!!!: p_point, curve, field
```
Format: --p_point X,Y --curve A0,A1,A2,A3,A4,A5,A6 --field FIELD --order_of_the_one_point

Example: --p_point 4,1 --curve 1,0,0,1,0,-1,1 --field 5 --order_of_the_one_point

Output:"    Given curve is elliptic.
            Elliptic curve: y^2 + 0 * y + 0 * xy = x^3 + 0 * x^2 - 1 * x + 1
            Order is: 4 "
```

## Order of all points on EC
- function for finding orders for all points for given curve
MUST GIVEN PARAMETER!!!: curve, field
```
Format: --curve A0,A1,A2,A3,A4,A5,A6 --field FIELD --order_of_all_point

Example: --curve 1,0,0,1,0,-1,1 --field 5 --order_of_all_point

Output:"    Given curve is elliptic.
            Elliptic curve: y^2 + 0 * y + 0 * xy = x^3 + 0 * x^2 - 1 * x + 1
            Given curve is elliptic.
            Elliptic curve: y^2 + 0 * y + 0 * xy = x^3 + 0 * x^2 - 1 * x + 1
            Orders    | Points
             1        | ['[∞,∞]']
             2        | [[3, 0]]
             4        | [[4, 1], [4, -1]]
             8        | [[0, 1], [0, -1], [1, 1], [1, -1]]  "
```

## MOV Attack
- provide MOV Attack on EC Diffie-Hellman
- need SECRET = E[P,aP], GENERATOR = E[P,P] and ORDER = order of EC
- output is secret value of a
```
Format: --mov_attack SECRET,GENERATOR,ORDER

Example: Known parameters: E[P,aP] = 5, E[P,P] = 2, order of EC is 10 --> write: --mov_attack 5,2,10

Output:"Secret is: 4"
```

## Possible orders of EC
- function for finding out possible order of points, if only order of EC (Elliptic curve) is known
- also function for finding out possible orders of points, if order of EC is change to given value
```
Formats: --possible_orders OLD_ORDER,NEW_ORDER
-in case we DO NOT change order of EC format is: --possible_orders ORDER

Example: --possible_orders 5,15

Output:"Possible orders are: [1, 5]"
```

## Bilinear operations
- function for getting overview of all bilinear operations
```
Format: --help_bilinear

Example: --help_bilinear

Output:"    e(P; O) = e(O; Q) = 1

            e(-P; Q) = e(P; Q)^1 = e(P; -Q)

            e(a * P; Q) = e(P; Q)^a = e(P; a * Q)

            e(a * P; b * Q) = e(P; Q)^(a*b)

            e(P1 + P2; Q) = e(P1; Q) * e(P2; Q) and e(P; Q1 + Q2) = e(P; Q1) * e(P; Q2)

            e(f(P); f(Q)) = f(e(P;Q)) where f is an automorphism (function)

            Weil pairing (in addition):

            e(P; Q) = e(Q; P)^(-1)

            e(P; P) = 1 "
```

## Z_x table

- function for generating help table of Z_x, which can be used for EC Diffie-Hellman.
```
Format: --get_z_x_table GENERATOR,MODULUS

Example: --get_z_x_table 2,5

Output:"    [1, 1, 1, 1]
            [1, 2, 4, 3]
            [1, 4, 1, 4]
            [1, 3, 4, 2]    "
```

## The training module

### tests
- function to practice some elliptic curve calculations 
```
Format: --tests
```
What happens?
+ Begin a semi-interactive terminal 
+ Answer 10 questions, then decide if you wish to continue

What types of questions are there?
+ Is a curve elliptic? Yes/No
+ Does this point belong on the curve? Yes/No
+ What are the possible orders of points for a curve? Num1, Num2, ..., NumX
+ What is the order of this curve? Num

##  Linear Congruential Generator (LCG)
- function for computation pseudorandom values by algorithm:
```
X_0 = s
X_1 = ( a * X_0 + c ) mod Prime
X_2 = ( a * X_1 + c ) mod Prime
...
```
- PRIME is prime number, A is a, C is c, SEED is s, COUNTER is number of random values to generate
```
Format:  --lcg PRIME,A,C,SEED,COUNTER

Example: --lcg 11,3,4,2,3

Output:"        LCG
                Number of random numbers is 3, prime p is 11, a = 3, c = 4 and seed X_0 = s = 2
                X_0 = 2
                X_1 = 10
                X_2 = 1 "
```
## R Value
- help function for One-bit Commitment function
```
Format:  --r_value R_1,R_2,R_3,...

Example: --r_value 1,0,1

Output:`NO OUTPUT
```
## One-bit Commitment
- function for demonstation of One-bit Commitment algorithm:
```
Alice                                   Bob
        System parameter: p is Prime number
                          G(s) is LCG function with a, c parameters

                                        Bob computes r and send it to Alice
        <-------------(r)--------------
Alice chooses seed s
Alice chooses commitment value b [bit]
If b is 0 secret C is computed by formula
        c= G(s) mod 2
Else:
        c = (G(s) mod 2) ⊕ r
Alice sends Bob secret c
        ---------------(c)------------>
...
Alice sends Bob opening (b,s)
        --------------(b,s)----------->
                                        Bob computes c' from opening values 
                                        and comperes it with c
```
- function **REQUIRE** enabling of **lcg** and **r_value** functions
```
Format:  --lcg PRIME,A,C,SEED,COUNTER --r_value R_1,R_2,R_3,... --one_bit_com B_COMMITMENT

Example: --lcg 11,3,4,2,3 --r_value 1,0,1 --one_bit_com 1

Output:"        LCG
                Number of random numbers is 3, prime p is 11, a = 3, c = 4 and seed X_0 = s = 2
                X_0 = 2
                X_1 = 10
                X_2 = 1
                One-bit Commitment
                Bob sends r = [1, 0, 1]
                Alice choose b = 1
                Alice sends c = [1, 0, 0]
                Alice sends opening (b,s) = (1, 2)      "
```
## Graph_a and Graph_b
- help function for Isomorphic function, gives information about edges of graphs
```
Format of EDGE: VERTICE_1,VERTICE_2

Format: --graph_a EDGE_1/EDGE_2/EDGE_3/...
        or
        --graph_b EDGE_1/EDGE_2/EDGE_3/...

Graph G1
    3   
   / \  
  2   4   
 /       
1   

Example for G1: --graph_a 1,2/2,3/3,4

Output: None      
```

## Isomorphic of Graphs
- function for deciding if two graphs are isomorphic
```
Graph G1  |  Graph G2
    3     |  
   / \    |   1   2
  2   4   |    \ / \
 /        |     3   4
1         |
```
2 Graphs are isomorphic, if they have:
+ same number of vertices
+ same number of edges
+ same degree
+ same "connections"

**Graph_a and Graph_b parameters are required!** 
```
Format: --graph_a EDGE_A_1/EDGE_A_2/... --graph_b EDGE_A_1/EDGE_A_2/... --is_isomorphic

Example: --graph_a 1,2/2,3/3,4 --graph_b 1,4/4,2/2,3 --is_isomorphic

Output:"        Isomorphic
                G1 = [1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]]
                G2 = [1, 2, 3, 4], [[1, 4], [4, 2], [2, 3]]
                 _____________________________________
                | Graph         | G1       | G2       |
                | # Vertices    | 4        | 4        |
                | # Edges       | 3        | 3        |
                | Degree        | 2        | 2        |
                | Connections   | Ok       | Ok       |
                |_______________|__________|__________|
                Graphs are Isomorphic!
                
                Permutation
                π = / 1, 2, 3, 4 \
                    \ 1, 4, 2, 3 /      "
```
## Permutation_1 and Permutation_2
- help function for giving permutation for Inverse Permutation, Composition and Permutation of Graph functions
```
Example of Permutation
π = / 1, 2, 3, 4 \    1. Line
    \ 1, 4, 2, 3 /    2. Line
```
- only second line is given as an argument for function
```
Format: --permutation_1 PERMUTATION
        or
        --permutation_2 PERMUTATION

Example: --permutation_1 1,4,2,3

Output: None
```
## Inverse Permutation
- function for computing of inverse permutation for given one  
- **Permutation_1 parameter is required!**
```
Format: --permutation_1 PERMUTATION --inverse_permutation

Example: --permutation_1 2,3,4,1 --inverse_permutation

Output:"        Permutation
                π = / 1, 2, 3, 4 \
                    \ 2, 3, 4, 1 /
                Inverse
                π^-1 = / 1, 2, 3, 4 \
                       \ 4, 1, 2, 3 /
                Composition
                            / 1, 2, 3, 4 \
                π ◦ π^-1 = |  4, 1, 2, 3  |
                            \ 1, 2, 3, 4 /      "
```
## Composition
- function for computing Composite of two given permutations
- **Permutation_1 and Permutation_2 parameters are required!**
```
Format: --permutation_1 PERMUTATION_1 --permutation_2 PERMUTATION_2 --composition

Example: --permutation_1 4,3,1,2 --permutation_2 4,1,2,3 --composition

Output:"        Composition
                            / 1, 2, 3, 4 \
                π ◦ π^-1 = |  4, 1, 2, 3  |
                            \ 2, 4, 3, 1 /        "
```
## Permutation of Graph
- function for doing permutation for given graph
- **Graph_a and Permutation_1 parameters are required!**
```
Format: --graph_a EDGE_A_1/EDGE_A_2/... --permutation_1 PERMUTATION --permut_graph 

Example: --graph_a 1,2/1,3/2,4/3,4/1,4 --permutation_1 2,3,4,1 --permut_graph 

Output:"        Permutation of Graph
                φ = / 1, 2, 3, 4 \
                    \ 2, 3, 4, 1 /
                Given Graph G = ([1, 2, 3, 4], [[1, 2], [1, 3], [2, 4], [3, 4], [1, 4]])
                New Graph Gx = ([1, 2, 3, 4], [[2, 3], [2, 4], [3, 1], [4, 1], [2, 1]]) "
```