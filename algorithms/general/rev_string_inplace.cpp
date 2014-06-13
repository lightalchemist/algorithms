
#include <string>
#include <iostream>

void reverse(std::string & s)
{
    if (s.size() == 0)
        return;

    char tmp;
    int i = 0;
    int j = s.size() - 1;
    while (i < j)
    {
        tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
        i += 1;
        j -= 1;
    }
}


int main(int argc, char *argv[])
{
    std::string s = "hello";
    reverse(s);
    std::cout << s << std::endl;

    s = "h";
    reverse(s);
    std::cout << s << std::endl;

    s = "";
    reverse(s);
    std::cout << s << std::endl;

    s = "batter";
    reverse(s);
    std::cout << s << std::endl;

    return 0;
}

