function solution(phone_number) {
  let repeatStars = "*".repeat(phone_number.length - 4);
  repeatStars += phone_number.substr(phone_number.length - 4, 4);
  return repeatStars;
}
