#include <bits/stdc++.h>
// This is not included in the course, just felt cool XD

using namespace std;

class GradientDescentForUnivariateLinearRegression{
public:
    vector<double> calculateLinearRegression(double w, double b, vector<double> x){
        int n = x.size();
        vector<double> y_hat; // this is gonna be the array of our predictions made using y = wx + b
        for(double x_i : x){
            double y_hat_i = (w*x_i) + b;
            y_hat.push_back(y_hat_i);
        }

        return y_hat; // return the simple linear model predicitons
    }

    double calculateLinearRegressionSingular(double w, double b, double x){
        double y_hat = (w*x) + b;
        return y_hat;
    }

    double computeCost(double w, double b, vector<double> x, vector<double> y){
        int n = y.size();
        double total_cost = 0;
        vector<double> y_hat = calculateLinearRegression(w,b,x); // here we will have the predicted values that are to be compared with the values provided in y vector
        
        for(int i = 0; i < n; i++){
            total_cost += pow((y_hat[i] - y[i]),2);
        }
        total_cost /= n*2;
    }

    pair<double,double> computeGradient(double w, double b, vector<double> x, vector<double> y){
        vector<double> y_hat = calculateLinearRegression(w,b,x);

        double dj_dw = 0;
        double dj_db = 0;
        int n = x.size();

        for(int i = 0; i < n; i++){
            double temp = (y_hat[i] - y[i]);
            dj_dw += temp*x[i];
            dj_db += temp;
        }
        dj_dw /= n;
        dj_db /= n;
    
    return make_pair(dj_dw,dj_db);
    }

    vector<vector<double>> computeGradientDescent(vector<double> x, vector<double> y, double w, double b, int num_iters, double alpha){
        vector<double> J_history;
        vector<double> W_history;
        vector<double> B_history;

        // run a number of iterations and record the values for w and b for each gradient

        while(num_iters--){
            pair<double,double> gradient = computeGradient(w,b,x,y);
            double djdw = gradient.first;
            double djdb = gradient.second;
            w -= djdw;
            b -= djdb;

            J_history.push_back(computeCost(w,b,x,y));
            W_history.push_back(w);
            B_history.push_back(b);

        }
            vector<vector<double>> result;
            vector<double>wb = {w,b};
            result.push_back(wb);
            result.push_back(J_history);
            result.push_back(W_history);
            result.push_back(B_history);

            return result;
    }
};