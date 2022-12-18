#include <iostream>
#include <random>
#include <vector>
#include <fstream>
#include <string>

int poker(int n) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dis(1, 52);

    int result = 0;
    for (int i = 0; i < n; i++) {
        std::vector<int> a[6];
        while (a->size() < 6) {
            int card = dis(gen);
            if (not std::count(a->begin(), a->end(), card)) {
                a->push_back(card);
            }
        }
        if (std::count(a->begin(), a->end(), 1) and std::count(a->begin(), a->end(), 2) and std::count(a->begin(), a->end(), 3) and std::count(a->begin(), a->end(), 4) and std::count(a->begin(), a->end(), 5)) {
            //std::cout << a->at(0) << " " << a->at(1) << " " << a->at(2) << " " << a->at(3) << " " << a->at(4) << " " << a->at(5) << " " << std::endl;
            result += 1;
        }
    }
    std::cout << result << std::endl;
    return result;
}

std::vector<int> dice(int n) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dis(1, 6);

    std::vector<int> result = {0, 0, 0, 0, 0, 0};

    for (int i = 0; i < n; i++) {
        int num = dis(gen);
        if (num == 1) {
            result[0] += 1;
        }
        else if (num == 2) {
            result[1] += 1;
        }
        else if (num == 3) {
            result[2] += 1;
        }
        else if (num == 4) {
            result[3] += 1;
        }
        else if (num == 5) {
            result[4] += 1;
        }
        else{
            result[5] += 1;
        }
    }
    return result;
}

std::vector<int> r_c_p(int n) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dis(1, 3);

    std::vector<int> result = { 0, 0, 0 };

    for (int i = 0; i < n; i++) {
        int user1 = dis(gen);
        int user2 = dis(gen);
        if (user1 == user2) {
            result[1] += 1;
        }
        else if (user1 == 1 and user2 == 2) {
            result[2] += 1;
        }
        else if (user1 == 1 and user2 == 3) {
            result[0] += 1;
        }
        else if (user1 == 2 and user2 == 1) {
            result[0] += 1;
        }
        else if (user1 == 2 and user2 == 3) {
            result[2] += 1;
        }
        else if (user1 == 3 and user2 == 1) {
            result[2] += 1;
        }
        else {
            result[0] += 1;
        }
    }
    return result;
}

std::vector<int> dice_sum(int n) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dis(1, 6);

    std::vector<int> result = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
    for (int i = 0; i < n; i++) {
        result[dis(gen) + dis(gen) - 2] += 1;
    }
    for (int i = 0; i < result.size(); i++) {
        std::cout << result[i] << " ";
    }
    std::cout << std::endl;
    return result;
}

void for_dice_sum(int n, int for_n) {
    std::vector<int> r = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
    std::vector<int> ds;
    for (int i = 0; i < for_n; i++) {
        ds = dice_sum(n);
        for (int j = 0; j < ds.size(); j++) {
            r[j] += ds[j];
        }
    }
    for (int i = 0; i < ds.size(); i++) {
        std::cout << r[i] << " ";
    }
    std::cout << std::endl;
}

void for_poker(int n, int for_n) {
    int r = 0;
    for (int i=0; i<for_n; i++)
        r += poker(n); //1000만
    std::cout << r;
}
void for_dice(int n, int for_n) {
    std::vector<int> r = {0, 0, 0, 0, 0, 0};
    std::vector<int> d;
    for (int i = 0; i < for_n; i++) {
        d = dice(n);
        std::cout << d[0] << " " << d[1] << " " << d[2] << " " << d[3] << " " << d[4] << " " << d[5] << std::endl;
        for (int j = 0; j < 6; j++) {
            r[j] += d[j];
        }
    }
    std::cout << r[0] << " " << r[1] << " " << r[2] << " " << r[3] << " " << r[4] << " " << r[5] << std::endl;
}
void for_rcp(int n, int for_n) {
    std::vector<int> r = {0, 0, 0};
    std::vector<int> rcp;
    for (int i = 0; i < for_n; i++) {
        rcp = r_c_p(n);
        std::cout << "win: " << rcp[0] << " tie: " << rcp[1] << " lose: " << rcp[2] << std::endl;
        for (int j = 0; j < 3; j++) {
            r[j] += rcp[j];
        }
    }
    std::cout << "win: " << r[0] << " tie: " << r[1] << " lose: " << r[2] << std::endl;
}

int main() {
    //for_poker(4331600, 100);
    //for_dice(60000000, 100);
    //for_rcp(60000000, 100);
    for_dice_sum(100000000, 100);
}
