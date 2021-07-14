#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

int main(){
	struct timeval t1, t2;
	gettimeofday(&t1,NULL);
	long long Fibo[3] = {1,1,0};
	long long min_num = 12345678999;
	//printf("min_num::");
	//scanf("%d",&min_num);
	long long max_num = 99987654321;
	//printf("max_num::");
	//scanf("%d",&max_num);
	//int *res;
	long long res[50];
	int j = 0;
	long long temp = 0;
	
	while(j < max_num){
		temp = Fibo[0] + Fibo[1];
		Fibo[2] = temp;
		if(temp >= min_num && temp <= max_num){
			//(int*)malloc((j+1)*sizeof(int));
			res[j] = temp;
			j += 1;
		}
		else if(temp > max_num){
			break;
		}
		temp = Fibo[1] + Fibo[2];
		Fibo[0] = temp;
		if(temp >= min_num && temp <= max_num){
			//(int*)malloc((j+1)*sizeof(int));
			res[j] = temp;
			j += 1;
		}
		else if(temp > max_num){
			break;
		}
		temp = Fibo[0] + Fibo[2];
		Fibo[1] = temp;
		if(temp >= min_num && temp <= max_num){
			//(int*)malloc((j+1)*sizeof(int));
			res[j] = temp;
			j += 1;
		}
		else if(temp > max_num){
			break;
		}
	}
	
	//printf("%llu",Fibo[0]);
	long long sum = 0;
	for(int i = 0; i < j; i++){
		sum += res[i];
	}
	printf("%llu\n",sum);
	gettimeofday(&t2,NULL);
	double runtime = (double)((double)(t2.tv_usec-t1.tv_usec)/1000000);
	printf("runtime::%.6fsec",runtime);
}
