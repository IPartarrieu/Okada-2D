//+
// Malla del dominio para Okada 2D. Aqui suponemos que la falla no es una recta
// sino un  rectangulo de un ancho muy pequegno
//
lc  = 10;      // tamagno de los elementos en el rectangulo grande
lc2 = 0.5;    // tamagno de los elementos en el rectangulo intermedio
lc3 = 0.01;   // tamagno de los elementos en la falla
//+
// Datos que definen la falla. La variable eps habla del ancho del rectangulo que define la falla
//
tip         = 3;
dip         = 40;
theta       = ((-90 + dip)/180.0)*Pi;
width       = 10;
eps         = 0.01;
//
// Puntos del 1 al 4 definen el rectangulo grande
//
//
//
//

// Todos los puntos

Point(1) = {0, 0, 0, lc};
//+
Point(2) = {100, 0, 0, lc};
//+
Point(3) = {100, -50, 0, lc};
//+
Point(4) = {85,-50,0,lc2};
//+
Point(5) = {75,-50,0,lc2};
//+
Point(6) = {0,-50,0,lc};
//+
Point(7) = {0,-25,0,lc2};
//+
Point(8) = {0,-15,0,lc2};
//+
Point(9) = {50,-15,0,lc2};
//+
Point(10) = {50,-25,0,lc2};
//+
Point(11) = {60.01, -25, 0, lc3};
//+
Point(12) = {65.8, -30.8, 0, lc3};
//+
Point(13) = {66, -30.6, 0, lc3};
//+
Point(14) = {60.21, -24.8, 0, lc3};

//
//
//
//
//

// Area Superior

Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 9};
//+
Line(5) = {9, 8};
//+
Line(6) = {8, 1};

//
//
//
//
//

// Area Intermedia

Line(7) = {8,9};
//+
Line(8) = {9,4};
//+
Line(9) = {4,5};
//+
Line(10) = {5,10};
//+
Line(11) = {10,7};
//+
Line(12) = {7,8};

//
//
//
//
//

// Area Inferior

Line(13) = {7,10};
//+
Line(14) = {10,5};
//+
Line(15) = {5,6};
//+
Line(16) = {6,7};

//
//
//
//
//

// Falla

Line(17) = {11,12};
//+
Line(18) = {12,13};
//+
Line(19) = {13,14};
//+
Line(20) = {14,11};

//
//
//
//
//

// Asignamos Loop

// Area Sup
Curve Loop(1) = {1,2,3,4,5,6};

// Area Int
Curve Loop(2) = {7,8,9,10,11,12};

// Area Inf
Curve Loop(3) = {13,14,15,16};

//Falla
Curve Loop(4) = {17,18,19,20};

//
//
//
//
//

// Superficies

Plane Surface(1) = {1,4};
//+
Plane Surface(2) = {2};
//+
Plane Surface(3) = {3};

//
//
//
//
//

// Condiciones Fisicas

Physical Curve("superficie",1) = {1};
//+
Physical Curve("profundidad",2) = {3,9,15};
//+
Physical Curve("derecha",3) = {2};
//+
Physical Curve("izquierda",4) = {6,16};
//+
Physical Curve("bordeg",5) = {12};
//+
Physical Curve("falla1",6) = {19};
//+
Physical Curve("falla2",7) = {17};

