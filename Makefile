CXX = g++
CXXFLAGS = -Wall -std=c++17

TARGET = App 

all: $(TARGET)

$(TARGET): App.cpp
	$(CXX) $(CXXFLAGS) $(CPPFLAGS) main.cpp $(LDFLAGS) -o $(TARGET)

clean:
	rm -f $(TARGET)