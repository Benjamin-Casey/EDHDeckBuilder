#include <string>
using namespace std;

class Group
{
public:
	Group(): name() { }
	Group(string name);
private:
	string name;
};
