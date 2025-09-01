CXX = g++
CXXFLAGS = -Wall -std=c++17 
LDFLAGS = -ljsoncpp

# Target name
TARGET = main

# Default rule
all: $(TARGET)

# Build the executable from main.cpp
$(TARGET): main.cpp
	$(CXX) $(CXXFLAGS) main.cpp -o $(TARGET)

# Clean up build files
clean:
	rm -f $(TARGET)