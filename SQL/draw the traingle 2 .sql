delimiter //

create procedure pattern()
begin 
  declare i int default 1;
  while i<21 do
    select repeat("* ",i);
    set i= i+1;
  end while;
end //

delimiter ;

call pattern()
