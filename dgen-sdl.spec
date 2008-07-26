Summary: DGen/SDL is a Sega Genesis (MegaDrive outside the US) emulator
Name: dgen-sdl 
Version: 1.23
Release: 3%{?dist}
License: BSD
Group: Applications/Emulators
URL: http://pknet.com/~joe/dgen-sdl.html 
Source: http://pknet.com/~joe/%{name}-%{version}.tar.gz
Patch0: dgen-sdl-1.23-gcc4.patch
Patch1: dgen-sdl-1.23-gcc34.patch
Patch2: dgen-sdl-1.23-man_warning.patch
Patch3: dgen-sdl-1.23-gzip_security_hole.patch
Patch4: dgen-sdl-1.23-command_line.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: SDL-devel >= 1.0.0
%ifarch %{ix86}
BuildRequires: nasm
%endif

%description
DGen/SDL is a semi-fantastic emulator for Unix-esque operating systems
supported by SDL library. It produces a virtual environment in which 
Sega Genesis (MegaDrive outside the US) games may run with fairly 
accurate audio and video.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
sed -i 's/\r//' mz80/mz80.txt

%build
%configure
# It does not compile with smp_mflags
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir docs
mkdir docs/mz80
cp -a mz80/mz80.txt docs/mz80
mkdir docs/star
cp -a star/stardoc.txt docs/star

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/dgen
%{_bindir}/tobin
%{_mandir}/man1/dgen.1*
%{_mandir}/man1/tobin.1*
%{_mandir}/man5/dgenrc.5*
%doc AUTHORS ChangeLog COPYING README sample.dgenrc
%doc docs/mz80 docs/star

%changelog
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
