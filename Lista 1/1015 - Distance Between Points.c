int main(void)
{
    float x1, x2, y1, y2;
    scanf("%f %f", &x1, &y1);
    scanf("%f %f", &x2, &y2);
    double distanciax = x2 - x1;
    distanciax = distanciax * distanciax;
    double distanciay = y2 - y1;
    distanciay = distanciay * distanciay;
    double distancia_final = (distanciax) + (distanciay);
    distancia_final = sqrt(distancia_final);
    printf("%.4lf\n", distancia_final);
}