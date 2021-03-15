#pragma once
#include <string>
#include "Group.h"
using namespace std;

// Note: potentially use a Card class rather than have strings.

class Deck
{
public:
	Deck() : commander(), name() { }
	Deck(string, string);
	void addCard(string card);
	void removeCard(string card);
private:
	string commander;
	string name;
};

