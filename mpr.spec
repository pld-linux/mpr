Summary: Poor man's memory profile
Name: mpr
Version: 1.8
Release: 1
Copyright: distributable
Group: Networking/Daemons
Source: ftp://sunsite.unc.edu/pub/Linux/devel/lang/c/mpr-1.8.tar.gz
Requires: gdb, gcc, binutils
ExclusiveArch: i386
ExclusiveOs: Linux
BuildRoot: /var/tmp/mpr-root

%description
mpr can be used to find malloc/realloc memory leaks and memory
allocation statistics and patterns - it does not find memory
corruption errors. It uses a simple, brute force strategy - log all
memory alloc/free requests to a file and then post-process this log
file once the program has terminated.


%changelog
* Tue May 19 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.8
- buildroot

* Wed Nov 26 1997 Otto Hammersmith <otto@redhat.com>
- fixed conflict with basename prototype

* Mon Apr 28 1997 Michael Fulbright <msf@redhat.com>
- Updated to version 1.6

* Tue Feb 25 1997 Michael Fulbright <msf@redhat.com>
- Cleaned up package, entered into powercd tree.

* Wed Feb 19 1997 Erik Troan <ewt@redhat.com>
- Initial version

%prep
%setup 
./configure x86-linux

%build
make CCFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib}
for n in mpr mprcc mprfl mprhi mprlk mprmap mprsz mprpc mprnm mprdem; do
	install -m 755 -o 0 -g 0 $n $RPM_BUILD_ROOT/usr/bin/$n
done
install -m 644 -o 0 -g 0 libmpr.a $RPM_BUILD_ROOT/usr/lib/libmpr.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README DOC FAQ BUGS LOG LICENSE README.PERL README.SLOW
/usr/lib/*
/usr/bin/*
