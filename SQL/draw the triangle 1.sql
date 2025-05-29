delimiter //
create procedure julia_patterns()
begin
  declare i int default 20;
  while i!=0 do
    select repeat("* ",i);
    set i = i-1;
  end while;
end //

delimiter ;

call julia_patterns();
