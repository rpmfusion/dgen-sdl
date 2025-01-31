Summary: A Sega Genesis (MegaDrive outside the US) emulator
Name: dgen-sdl 
Version: 1.33
Release: 20%{?dist}
License: BSD
URL: http://dgen.sourceforge.net/
Source: http://downloads.sourceforge.net/dgen/%{name}-%{version}.tar.gz
BuildRequires: SDL-devel >= 1.0.0
BuildRequires: libarchive-devel
BuildRequires: gcc-c++
%ifarch %{ix86}
BuildRequires: nasm
%endif

%description
DGen/SDL is an emulator for the Sega Genesis/MegaDrive game console. It 
supports save states, full screen mode, interlace mode, Game Genie, joystick, 
compressed ROM images, and more. 


%prep
%setup -q

# Fix file encoding
for txtfile in cz80/readme.txt star/stardoc.txt
do
    iconv --from=ISO-8859-1 --to=UTF-8 $txtfile > tmp
    touch -r $txtfile tmp
    mv tmp $txtfile
done

# Fix build with nasm 2.13.01
sed -i '/@NASM@/s/--//' \
  Makefile.in \
  mz80/Makefile.in \
  star/Makefile.in


%build
%configure
# It does not compile with smp_mflags
make V=1


%install
%make_install

# install docs
mkdir docs
mkdir docs/cyclone
cp -a cyclone/Cyclone.txt docs/cyclone
mkdir docs/cz80
cp -a cz80/readme.txt docs/cz80
mkdir docs/drz80
cp -a drz80/DrZ80.txt docs/drz80
mkdir docs/dz80
cp -a dz80/FILE_ID.DIZ docs/dz80
cp -a dz80/README.TXT docs/dz80
cp -a dz80/whatsnew.txt docs/dz80
mkdir docs/musa
cp -a musa/readme.txt docs/musa
cp -a musa/history.txt docs/musa
mkdir docs/mz80
cp -a mz80/mz80.txt docs/mz80
mkdir docs/star
cp -a star/stardoc.txt docs/star

# remove not useful binary file
rm -f %{buildroot}%{_bindir}/cyclone


%files
%{_bindir}/dgen
%{_bindir}/dgen_tobin
%{_mandir}/man1/dgen.1*
%{_mandir}/man1/dgen_tobin.1*
%{_mandir}/man5/dgenrc.5*
%license COPYING
%doc AUTHORS ChangeLog README sample.dgenrc
%doc docs/cyclone docs/cz80 docs/drz80 docs/dz80 docs/musa docs/mz80 docs/star


%changelog
* Wed Jan 29 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.33-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.33-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.33-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.33-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.33-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.33-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.33-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.33-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.33-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.33-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.33-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.33-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.33-8
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 1.33-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.33-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 02 2017 Andrea Musuruane <musuruan@gmail.com> - 1.33-5
- fixed build with nasm 2.13.01

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Aug 17 2014 Andrea Musuruane <musuruan@gmail.com> - 1.33-3
- fixed building on arm

* Sat Aug 16 2014 Andrea Musuruane <musuruan@gmail.com> - 1.33-2
- fixed building on arm
- added missing cpu emulators docs
- dropped obsolete Group, Buildroot, %%clean and %%defattr
- dropped cleaning at the beginning of %%install

* Sun Jul 27 2014 Andrea Musuruane <musuruan@gmail.com> - 1.33-1
- updated to new upstream version

* Sun Feb 10 2013 Andrea Musuruane <musuruan@gmail.com> - 1.32-1
- updated to new upstream version

* Fri Feb 08 2013 Andrea Musuruane <musuruan@gmail.com> - 1.31-2
- rebuilt due to libarchive soname bump

* Mon Nov 26 2012 Andrea Musuruane <musuruan@gmail.com> 1.31-1
- updated to new upstream version

* Sun Mar 11 2012 Andrea Musuruane <musuruan@gmail.com> 1.30-1
- updated to new upstream version

* Thu Mar 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.29-2
- Rebuilt for c++ ABI breakage

* Sat Feb 04 2012 Andrea Musuruane <musuruan@gmail.com> 1.29-1
- updated to new upstream version

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

* Fri Dec 01 2006 Andrea Musuruane <musuruan@gmail.com> 1.23-2
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
