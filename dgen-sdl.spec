Summary: A Sega Genesis (MegaDrive outside the US) emulator
Name: dgen-sdl 
Version: 1.28
Release: 1%{?dist}
License: BSD
Group: Applications/Emulators
URL: http://dgen.sourceforge.net/
Source: http://downloads.sourceforge.net/dgen/%{name}-%{version}.tar.gz
# Fix man page warnings
# http://sourceforge.net/tracker/?func=detail&aid=3455451&group_id=227519&atid=1070824
Patch0: dgen-sdl-1.28-man_warning.patch
# Fix not to require an executable stack
# http://sourceforge.net/tracker/?func=detail&aid=3457405&group_id=227519&atid=1070824
Patch1: dgen-sdl-1.28-execstack.patch 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: SDL-devel >= 1.0.0
BuildRequires: libarchive-devel
%ifarch %{ix86}
BuildRequires: nasm
%endif

%description
DGen/SDL is an emulator for the Sega Genesis/MegaDrive game console. It 
supports save states, full screen mode, interlace mode, Game Genie, joystick, 
compressed ROM images, and more. 

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# Fix file encoding
for txtfile in cz80/readme.txt
do
    iconv --from=ISO-8859-1 --to=UTF-8 $txtfile > tmp
    touch -r $txtfile tmp
    mv tmp $txtfile
done

%build
%configure
# It does not compile with smp_mflags
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir docs
mkdir docs/cz80
cp -a cz80/readme.txt docs/cz80
mkdir docs/musa
cp -a musa/readme.txt docs/musa
cp -a musa/history.txt docs/musa
mkdir docs/mz80
cp -a mz80/mz80.txt docs/mz80
mkdir docs/star
cp -a star/stardoc.txt docs/star

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/dgen
%{_bindir}/dgen_tobin
%{_mandir}/man1/dgen.1*
%{_mandir}/man1/dgen_tobin.1*
%{_mandir}/man5/dgenrc.5*
%doc AUTHORS ChangeLog COPYING README sample.dgenrc
%doc docs/cz80 docs/musa docs/mz80 docs/star

%changelog
* Sun Dec 11 2011 Andrea Musuruane <musuruan@gmail.com> 1.28-1
- updated to new upstream version
- updated URL and Source tags
- updated summary and description
- dropped no longer needed patches
- submitted patches upstream

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.23-5
- rebuild for new F11 features

* Wed Aug 06 2008 Andrea Musuruane <musuruan@gmail.com> 1.23-4
- added a patch not to require an executable stack
- new upstream developer - updated URL and Source tags

* Mon Nov 26 2007 Andrea Musuruane <musuruan@gmail.com> 1.23-3
- removed %%{?dist} tag from changelog
- removed %%{?_smp_mflags} from make invocation

* Sat Dec 01 2006 Andrea Musuruane <musuruan@gmail.com> 1.23-2
- source tarball now matches upstreams
- added MZ80 and Starscream docs

* Sat Nov 18 2006 Andrea Musuruane <musuruan@gmail.com> 1.23-1
- first release for Dribble based on the old Falsehope package 
- fixed Summary tag
- updated URL and Source tag
- fixed License tag
- changed BuildRoot to meet Fedora guidelines
- added SDL-devel to BuildRequires
- fixed BuildRequires to add nasm if arch is %%{ix86} and not only i386
- removed Requires tag
- removed Packager tag
- using %%configure macro instead of configure
- added %%{?_smp_mflags} to make invocation to speed up SMP builds
- cleaning of buildroot in %%install
- fixed %%files
- added a patch from Stephen Bridges to fix gcc4 compiling (Gentoo #133203)
- added a patch to fix gcc-3.4 compiling (Gentoo #116113) 
- added a patch from Debian to fix man warning on dgenrc(5)
- added a patch from Debian to fix file-in-tmp security hole in gzip/bzip 
  rom extraction code (Debian #263282)
- added a patch from Debian to allows the SDL interface to set the fullscreen 
  and scale values using the values from the RC file, even if there are no 
  command-line options

* Tue Jul 03 2001 Henri Gomez <hgomez@slib.fr>
- dgen-sdl 1.2.3
- built against SDL 1.2.1

* Mon Aug 21 2000 Henri Gomez <hgomez@slib.fr>
- patch for 1.0 and 1.1 support (thanks to Joe Groff (ognir@humboldtl.com)
- recompiled with sdl 1.1 

* Tue Jun 13 2000 Henri Gomez <hgomez@slib.fr>
- Initial RPM release
- for i386 platform use nasm for better performance.
- Built under Redhat 6.1 with updates.
