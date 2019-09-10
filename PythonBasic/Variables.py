x = 2;
y = 1.8;
z = "hello";
a = 35e3;
b = "hello world!    ";
c = "HELLO WORLD!";
# Int
print(type(x));
# Float
print(type(y));
# String
print(type(z));
# float
print(type(a));
# Get a character from a string by position
print(z[3]);
# Split a string from a string
print(z[0:3]);
# Trim a string
print(b.strip());
# Return length of string
print(len(b));
# Upper case a string
print(b.upper());
# Lower case a string
print(c.lower());
# Replace
print(c.replace("WORLD","THINH"));
# Command line string input
print("Enter a name:");
name = input();
print("Hello "+ name.upper());
# Repeat a string
print("Hello "*3)